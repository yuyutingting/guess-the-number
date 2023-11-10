import random
import xml.etree.ElementTree as ET

def load_config():
    tree = ET.parse('config.xml')
    root = tree.getroot()
    x1 = int(root.find('x1').text)
    x2 = int(root.find('x2').text)
    n = int(root.find('n').text)
    return x1, x2, n

def save_config(x1, x2, n):
    root = ET.Element("config")
    ET.SubElement(root, "x1").text = str(x1)
    ET.SubElement(root, "x2").text = str(x2)
    ET.SubElement(root, "n").text = str(n)
    tree = ET.ElementTree(root)
    tree.write('config.xml')

def guess_the_number(x1, x2, max_attempts):
    target_number = random.randint(x1, x2)
    attempts = 0

    print(f"猜一個在 {x1} 到 {x2} 之間的數字。")

    while attempts < max_attempts:
        guess = int(input("你的猜測是："))

        if guess == target_number:
            print(f"恭喜！你猜對了，目標數字是 {target_number}。")
            break
        elif guess < target_number:
            print("太低了，再試一次。")
        else:
            print("太高了，再試一次。")

        attempts += 1

    if attempts == max_attempts:
        print(f"很抱歉，你已經猜了 {max_attempts} 次，遊戲結束。正確答案是 {target_number}。")

if __name__ == "__main__":
    try:
        x1, x2, n = load_config()
    except FileNotFoundError:
        print("找不到配置文件。使用默認值。")
        x1, x2, n = 1, 100, 10

    guess_the_number(x1, x2, n)
