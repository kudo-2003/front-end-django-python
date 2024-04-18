import os
import sys
import webbrowser

def open_browser():
    webbrowser.open_new("http://127.0.0.1:8000/ShopDBA/index")

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'QuangHung94079_kuDo_shinichi.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Không thể nhập Django. Bạn có chắc chắn rằng nó đã được cài đặt và khả dụng trên biến môi trường PYTHONPATH của bạn không? Bạn đã quên kích hoạt môi trường ảo?") from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    open_browser()
    main()
