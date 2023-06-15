import cv2

# 01. 일반이미지
# img = cv2.imread('./Day07/test.jpg')

# 02. 흑백이미지
# img = cv2.imread('./Day07/test.jpg', cv2.IMREAD_GRAY

# 04. 원븐을 그대로 두고 흑백을 추가
img = cv2.imread('./Day07/test.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 03.  이미지 사이즈 축소
# img_small = cv2.resize(img, (200, 120))

# 05. 이미지 자르기
height, width, channel = img.shape
img_crop = img[:, :int(width/2)] # height, width
gray_crop = gray[:, :int(width/2)]

# 06. 이미지 블러
img_blur = cv2.blur(img_crop, (10, 10)) # 숫자가 클수록 더 많이 블러(흐릿하게)

cv2.imshow('blur half', img_blur)
cv2.imshow('Gray half', gray_crop)

cv2.waitKey(0)
cv2.destroyAllWindows()