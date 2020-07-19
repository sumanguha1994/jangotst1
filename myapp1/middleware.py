class JSONTranslationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.translations = {
            "en"   : {
                        "greeting": "Hello", 
                        "msg": "Welcome Here", 
                        "content": "This is under a block content", 
                        "koyel": "Welcome Koyel",
                        "pertional_page": "IT's you pertional page",
                        "generaic_static_page": "IT's a Generic static page.",
                        "staticview_method": "Call this page by StaticView method from view && myapp1url.p"
                    },
            "hi"   : {
                        "greeting": "हैलो", 
                        "msg": "स्वागत है", 
                        "content": "यह एक ब्लॉक सामग्री के तहत है", 
                        "koyel": "आपका स्वागत है कोयल",
                        "pertional_page": "यह आपको प्रासंगिक पृष्ठ है",
                        "generaic_static_page": "यह एक सामान्य स्थिर पृष्ठ है।",
                        "staticview_method": "इस पेज को StaticView पद्धति से view && myapp1url.p पर कॉल करें"
                    },
            "ar"   : {
                        "greeting": "مرحبا", 
                        "msg": "اهلا بك هنا",
                        "content": "هذا تحت محتوى كتلة", 
                        "koyel": "اهلا وسهلا بك",
                        "pertional_page": "أنت صفحة ذات الصلة",
                        "generaic_static_page": "إنها صفحة ثابتة عامة",
                        "staticview_method": "استدعاء هذه الصفحة بطريقة StaticView من العرض && myapp1url.py"
                    },
            "jp"   : {
                        "greeting": "こんにちは", 
                        "msg": "ここへようこそ", 
                        "content": "これはブロックコンテンツの下にあります", 
                        "koyel": "ようこそコエル",
                        "pertional_page": "それはあなたのパーショナルページです",
                        "generaic_static_page": "これは汎用静的ページです",
                        "staticview_method": "ビューからstaticviewメソッドでこのページを呼び出します && myapp1url.py"
                    },
            "bn"   : {
                        "greeting": "হ্যালো", 
                        "msg": "এখানে স্বাগতম",
                        "content": "এটি একটি ব্লক সামগ্রীর অধীনে", 
                        "koyel": "স্বাগতম কোয়েল",
                        "pertional_page": "এটি আপনি প্যারেশনাল পৃষ্ঠা",
                        "generaic_static_page": "এটি একটি জেনেরিক স্ট্যাটিক পৃষ্ঠা।",
                        "staticview_method": "এই পৃষ্ঠাটি দেখুন থেকে স্ট্যাটিকভিউ পদ্ধতিতে কল করুন && myapp1url.py"
                    }
        }
    
    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        response.context_data["translations"] = self.translations
        return response

