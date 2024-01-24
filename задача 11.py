def image_info (img):
    if ('image_id' not in img) or ('image_title' not in img):
        raise TypeError('Image')
    return f"Image {img ['image_title']} has id {img['image_id']}"


print(image_info({'image_id': '12323', 'image_title': 'My_cate'}))

try:
    print(image_info({'image_id': '12323'}))
except TypeError as e:
    print(e)