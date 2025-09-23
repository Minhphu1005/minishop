from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps


def admin_required(view_func):
    """
    Decorator để yêu cầu user phải là admin (staff hoặc superuser)
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Bạn cần đăng nhập để truy cập trang này.')
            return redirect('accounts:login')
        
        if not (request.user.is_staff or request.user.is_superuser):
            messages.error(request, 'Bạn không có quyền truy cập trang này.')
            return redirect('products:product_list')
        
        return view_func(request, *args, **kwargs)
    return wrapper


def superuser_required(view_func):
    """
    Decorator để yêu cầu user phải là superuser
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Bạn cần đăng nhập để truy cập trang này.')
            return redirect('accounts:login')
        
        if not request.user.is_superuser:
            messages.error(request, 'Chỉ có superuser mới có quyền truy cập trang này.')
            return redirect('products:product_list')
        
        return view_func(request, *args, **kwargs)
    return wrapper


def is_admin(user):
    """
    Helper function để kiểm tra user có phải admin không
    """
    return user.is_authenticated and (user.is_staff or user.is_superuser)


def is_superuser(user):
    """
    Helper function để kiểm tra user có phải superuser không
    """
    return user.is_authenticated and user.is_superuser