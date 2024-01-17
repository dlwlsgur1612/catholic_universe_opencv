import cv2


def main():
    img = cv2.imread(
        "/home/jh/catholic_universe_opencv/opencv/data/lena.jpg", 1
    )
    # img = cv2.imread("opencv_learning/isw.py", 1)
    print(cv2.__version__)
    cv2.imshow("lena", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()