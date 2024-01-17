import cv2


def main():
    img = cv2.imread(
        "/home/jh/catholic_universe_opencv/opencv/data/lena.jpg", 1
    )
    cv2.imwrite(
        "", img
    )
    cv2.imwrite(
        "", img
    )
    cv2.imwrite(
        "",
        img,
        [cv2.IMWRITE_JPEG_QUALITY, 50],
    )
    cv2.imwrite(
        "",
        img,
        [cv2.IMWRITE_JPEG_QUALITY, 8],
    )


if __name__ == "__main__":
    main()