# app/utils/pagination.py
from flask import request, url_for

DEFAULT_PER_PAGE = 50
MAX_PER_PAGE = 200

def get_pagination_params():
    page = max(int(request.args.get("page", 1)), 1)
    per_page = min(max(int(request.args.get("per_page", DEFAULT_PER_PAGE)), 1), MAX_PER_PAGE)
    return page, per_page

def envelope(query, page, per_page, endpoint, **endpoint_kwargs):
    items = query.paginate(page=page, per_page=per_page, error_out=False)
    def link(p):
        if p is None: return None
        return url_for(endpoint, page=p, per_page=per_page, _external=True, **endpoint_kwargs)
    return {
        "data": items.items,
        "meta": {"page": items.page, "per_page": per_page, "pages": items.pages, "total": items.total},
        "links": {"self": link(items.page), "next": link(items.next_num), "prev": link(items.prev_num)}
    }
