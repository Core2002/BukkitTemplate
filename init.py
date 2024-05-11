import os

tip = '''正在初始化模板项目...
请输入项目名

注意：
使用纯英文+空格的方式书写，首字母大写。
请不要使用中文、斜杠、减号、下划线

例： Bukkit Template
请输入：
'''

projectName = input(tip)
projectName_NoSpaces = projectName.replace(' ', '')
packageName = projectName_NoSpaces.lower()


def replaceTextFile(filePath: str, old: str, new: str, ec: str = 'UTF-8'):
    text = ""
    with open(filePath, encoding=ec, mode='r') as file:
        text = file.read()
    with open(filePath, encoding=ec, mode='w') as file:
        file.write(text.replace(old, new))


replaceList = [
    "settings.gradle",
    "README.md",
    "build.gradle",
    "src/main/resources/plugin.yml",
    "src/main/java/fun/fifu/bukkittemplate/BukkitTemplate.java",
    "src/main/java/fun/fifu/bukkittemplate/Main.java",
]

for path in replaceList:
    replaceTextFile(path, "BukkitTemplate", projectName_NoSpaces)
    replaceTextFile(path, "Bukkit Template", projectName)
    replaceTextFile(path, "bukkittemplate", packageName)

base = "src/main/java/fun/fifu"
os.rename(f"{base}/bukkittemplate/BukkitTemplate.java",
          f"{base}/bukkittemplate/{projectName_NoSpaces}.java")
os.rename(f"{base}/bukkittemplate", f"{base}/{packageName}")

print("完毕\n使用 'gradlew build' 来编译项目")

os.remove(os.path.realpath(__file__))
