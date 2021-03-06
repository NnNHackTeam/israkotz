"""Autocomplete support for foreign keys.
Requires the protoculous JavaScript library."""

# Widget

# originally from http://www.djangosnippets.org/snippets/253/

from django import newforms as forms
from django.newforms.widgets import TextInput, flatatt
from django.newforms.util import smart_unicode

from django.utils.html import escape

class AutoCompleteField(TextInput):
    def __init__(self, url='', options=None, attrs=None):
        self.url = url
        self.options = {'paramName': 'text'}
        if options:
            self.options.update(options)
        if attrs is None:
            attrs = {}
        self.attrs = attrs

    def render(self, name, value=None, attrs=None):
        final_attrs = self.build_attrs(attrs, name=name)
        if value:
            value = smart_unicode(value)
            final_attrs['value'] = escape(value)
        if not self.attrs.has_key('id'):
            final_attrs['id'] = 'id_%s' % name
        return (u'''<input type="text"%(attrs)s /><div class="autocomplete" id="box_%(name)s"></div>
<script type="text/javascript">new Ajax.Autocompleter('%(id)s', 'box_%(name)s', '%(url)s', %(options)s);</script>'''
        ) % {
            'attrs': flatatt(final_attrs),
            'name': name,
            'id': final_attrs['id'],
            'url': self.url,
            'options': plist_from_dict(self.options)
        }

def plist_from_dict(d):
    """Convert a Python dict into a JavaScript property list.
    The order of the items in the returned string is undefined."""
    return '{' + ', '.join(['%s: %r' % kv for kv in d.items()]) + '}'

# Query helper

from django.db.models import Model, Q

def autocomplete_query(text, model_or_qs, fields):
    """Return just those rows of model that contain
    all of the words of text in the fields string list.

    Instead of a Model class, you may also pass an initial QuerySet
    instance, e.g. for prefiltering or setting a different order.

    If a field name starts with a caret (^), the term is a prefix match
    (field LIKE "word%"), otherwise it is a full search (field LIKE "%word%")."""

    # check if a Model or a QuerySet was passed
    if issubclass(model_or_qs, Model):
        qs = model_or_qs.objects.all()
    else:
        qs = model_or_qs

    # pre-calculate the filter terms, they'll be user once per word
    terms = [
        f.startswith('^') and f[1:] + '__istartswith' or f + '__icontains'
        for f in fields
    ]

    # look for each word in every field -- this queryset represents
    # the statement
    #
    # SELECT * FROM model_or_qs
    # WHERE (field1 LIKE '%word1%' OR field2 LIKE '%word1%' OR ...)
    #   AND (field1 LIKE '%word2%' OR field2 LIKE '%word2%' OR ...)
    #   AND (field1 LIKE ...)
    #   ...
	#
    for word in text.split():
        q = Q()
        for term in terms:
            q = q | Q(**{term: word})
        qs = qs.filter(q)

    return qs

# View helper

from django.http import HttpResponse

def autocomplete_response(text, model_or_qs, fields, max_count=50):
    """Return the unordered list that is required by the Ajax.AutoCompleter.
    The field value will be the item's id; its __str__ is displayed
    along with it, but not stored."""

    qs = autocomplete_query(text, model_or_qs, fields)
    if qs.count() > max_count:
        result = [(0, _('Too many results, please enter more'))]
    else:
        result = [(d.id, '%s' % d) for d in qs]
    result = '\n'.join([
        '<li>%d<span class="informal">) %s</span></li>' % (id, escape(name))
        for id, name in result
    ])

    return HttpResponse('<ul>' + result + '</ul>')