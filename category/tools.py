from django.utils.translation import ugettext_lazy as _
from django.template import RequestContext
from django.shortcuts import render_to_response

import object_tools

from category.models import Category


class Delete(object_tools.ObjectTool):
    name = "tree"
    label = _("Tree")

    def view(self, request, extra_context=None):
        return render_to_response(
            "admin/category/tree.html",
            {"categories" : Category.objects.filter(
                parent=None).order_by("title")
            },
            RequestContext(request, {}),
        )


object_tools.tools.register(Delete, Category)
