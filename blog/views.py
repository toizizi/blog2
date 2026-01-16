from django.shortcuts import render

def home(request):
    life_posts = [
        {
            'image': 'pic\猫.jpg', 
            'title': 'maomao',
            'desc': '哈哈哈哈不好意思小猫，你正经的样子好好笑，我下次还会去百伦看你的，嘻嘻'
        },
        {
            'image': 'pic\神诞树.jpg',
            'title': '美呆的圣诞树',
            'desc': '不知道为啥留着这张照片，但我始终觉得这张照片我以前非常想保存下来，就留下来直到想起来那天吧，不过树还是很美的'
        },
        {
            'image': 'pic\奶皮子.jpg',
            'title': '新疆奶皮子',
            'desc': '麻蛋，网上炒的那么好喝，也只有前几口能品出来不错，后面给我牙甜疼了，此生不愿回味第二次!(just a kidding,只是牙疼很生气。。)'
        }
    ]

    return render(request, 'index.html', {
        'life_posts': life_posts
    })
