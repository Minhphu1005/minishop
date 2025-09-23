from django.core.management.base import BaseCommand
from django.utils.text import slugify
from products.models import Category, Product
from decimal import Decimal


class Command(BaseCommand):
    help = 'Tạo dữ liệu mẫu cho sản phẩm'

    def handle(self, *args, **options):
        # Tạo danh mục
        categories_data = [
            {'name': 'Điện thoại', 'description': 'Điện thoại thông minh các hãng'},
            {'name': 'Laptop', 'description': 'Máy tính xách tay văn phòng và gaming'},
            {'name': 'Thời trang', 'description': 'Quần áo, giày dép thời trang'},
            {'name': 'Gia dụng', 'description': 'Đồ dùng gia đình tiện ích'},
            {'name': 'Sách', 'description': 'Sách học tập và giải trí'},
        ]
        
        categories = []
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={
                    'slug': slugify(cat_data['name']),
                    'description': cat_data['description']
                }
            )
            categories.append(category)
            if created:
                self.stdout.write(f'Tạo danh mục: {category.name}')

        # Tạo sản phẩm
        products_data = [
            # Điện thoại
            {'name': 'iPhone 15 Pro Max', 'category': 'Điện thoại', 'price': 29990000, 'stock': 50, 
             'description': 'iPhone 15 Pro Max với chip A17 Pro mạnh mẽ, camera 48MP chuyên nghiệp và màn hình Super Retina XDR 6.7 inch'},
            {'name': 'Samsung Galaxy S24 Ultra', 'category': 'Điện thoại', 'price': 28990000, 'stock': 45,
             'description': 'Galaxy S24 Ultra với S Pen tích hợp, camera zoom 100x và hiệu năng vượt trội với Snapdragon 8 Gen 3'},
            {'name': 'Xiaomi 14 Pro', 'category': 'Điện thoại', 'price': 15990000, 'stock': 60,
             'description': 'Xiaomi 14 Pro với camera Leica, chip Snapdragon 8 Gen 3 và sạc nhanh 120W'},
             
            # Laptop
            {'name': 'MacBook Air M2', 'category': 'Laptop', 'price': 27990000, 'stock': 30,
             'description': 'MacBook Air M2 13 inch với hiệu năng vượt trội, thời lượng pin cả ngày và thiết kế siêu mỏng'},
            {'name': 'Dell XPS 13', 'category': 'Laptop', 'price': 23990000, 'stock': 25,
             'description': 'Dell XPS 13 với màn hình InfinityEdge, vi xử lý Intel Core i7 thế hệ mới nhất'},
            {'name': 'Asus ROG Strix G15', 'category': 'Laptop', 'price': 19990000, 'stock': 20,
             'description': 'Laptop gaming Asus ROG Strix G15 với RTX 4060, AMD Ryzen 7 và màn hình 144Hz'},
             
            # Thời trang
            {'name': 'Áo sơ mi nam công sở', 'category': 'Thời trang', 'price': 299000, 'stock': 100,
             'description': 'Áo sơ mi nam cao cấp, chất liệu cotton 100%, phù hợp đi làm và dự tiệc'},
            {'name': 'Giày sneaker nữ', 'category': 'Thời trang', 'price': 599000, 'stock': 80,
             'description': 'Giày sneaker nữ thời trang, đế êm ái, phong cách năng động'},
            {'name': 'Túi xách nữ da thật', 'category': 'Thời trang', 'price': 899000, 'stock': 40,
             'description': 'Túi xách nữ da thật cao cấp, thiết kế sang trọng, nhiều ngăn tiện lợi'},
             
            # Gia dụng
            {'name': 'Nồi cơm điện Panasonic', 'category': 'Gia dụng', 'price': 1290000, 'stock': 35,
             'description': 'Nồi cơm điện Panasonic 1.8L với công nghệ fuzzy logic, cơm ngon như nấu bếp than'},
            {'name': 'Máy xay sinh tố Philips', 'category': 'Gia dụng', 'price': 890000, 'stock': 50,
             'description': 'Máy xay sinh tố Philips công suất lớn, lưỡi dao sắc bén, dễ dàng làm sạch'},
            {'name': 'Bàn ủi hơi nước Tefal', 'category': 'Gia dụng', 'price': 590000, 'stock': 25,
             'description': 'Bàn ủi hơi nước Tefal với đế ceramic, hơi nước mạnh, ủi phẳng mọi loại vải'},
             
            # Sách
            {'name': 'Đắc Nhân Tâm', 'category': 'Sách', 'price': 79000, 'stock': 200,
             'description': 'Cuốn sách kinh điển về nghệ thuật giao tiếp và ứng xử của Dale Carnegie'},
            {'name': 'Sapiens - Lược sử loài người', 'category': 'Sách', 'price': 159000, 'stock': 150,
             'description': 'Tác phẩm của Yuval Noah Harari về lịch sử và tương lai của loài người'},
            {'name': 'Nhà giả kim', 'category': 'Sách', 'price': 89000, 'stock': 180,
             'description': 'Tiểu thuyết triết lý nổi tiếng của Paulo Coelho về hành trình tìm kiếm ước mơ'},
        ]
        
        for prod_data in products_data:
            category = Category.objects.get(name=prod_data['category'])
            product, created = Product.objects.get_or_create(
                name=prod_data['name'],
                defaults={
                    'slug': slugify(prod_data['name']),
                    'category': category,
                    'price': Decimal(str(prod_data['price'])),
                    'stock': prod_data['stock'],
                    'description': prod_data['description'],
                    'available': True
                }
            )
            if created:
                self.stdout.write(f'Tạo sản phẩm: {product.name}')

        self.stdout.write(
            self.style.SUCCESS('Tạo dữ liệu mẫu thành công!')
        )
