from rest_framework.pagination import PageNumberPagination


class CitySearchPagination(PageNumberPagination):
    """
    Custom pagination class for city search results.
    """
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100
