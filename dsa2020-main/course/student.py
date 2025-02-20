from person import Person

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade
    
    # 内置sort函数，引用 < 比较符来判断前后
    def __lt__(self, other):
        # 姓名字母顺序在前就排前面
        return self.name < other.name

    # Student的易懂字符串表示
    def __str__(self):
        return "({},{})".format(self.name, self.grade)

    # Student的正式字符串表示，与易懂表示相同
    __repr__ = __str__


if __name__ == "__main__":
    # 构造一个Python List对象
    s = list()

    # 添加5个Student对象到List中
    s.append(Student("Jack", 80))
    s.append(Student("Jane", 75))
    s.append(Student("Smith", 82))
    s.append(Student("Cook", 90))
    s.append(Student("Tom", 70))
    print("Original:", s)

    # 对List进行排序，注意这是内置sort方法
    s.sort()

    # 查看排序结果：按成绩高低排序
    print("Sorted:", s)
