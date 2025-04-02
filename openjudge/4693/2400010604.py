class Node:
    def __init__(self, coef=0, exp=0, next_node=None):
        self.coef = coef
        self.exp = exp
        self.next = next_node

def create_polynomial():
    poly = Node()  # 头结点
    current = poly
    while True:
        inputs = input().split()
        for i in range(0, len(inputs), 2):
            coef = int(inputs[i])
            exp = int(inputs[i+1])
            if coef == 0 and exp == 0:
                return poly
            new_node = Node(coef, exp)
            current.next = new_node
            current = new_node

def add_polynomials(A, B):
    dummy = Node()
    current = dummy
    p1 = A.next
    p2 = B.next

    while p1 and p2:
        if p1.exp > p2.exp:
            current.next = Node(p1.coef, p1.exp)
            p1 = p1.next
            current = current.next
        elif p1.exp < p2.exp:
            current.next = Node(p2.coef, p2.exp)
            p2 = p2.next
            current = current.next
        else:
            coef_sum = p1.coef + p2.coef
            if coef_sum != 0:
                current.next = Node(coef_sum, p1.exp)
                current = current.next
            p1 = p1.next
            p2 = p2.next

    if p1:
        current.next = p1
    elif p2:
        current.next = p2

    return dummy

def multiply_polynomials(A, B):
    result = Node()
    p1 = A.next

    while p1:
        p2 = B.next
        temp_list = Node()
        temp_current = temp_list

        while p2:
            new_coef = p1.coef * p2.coef
            new_exp = p1.exp + p2.exp
            temp_current.next = Node(new_coef, new_exp)
            temp_current = temp_current.next
            p2 = p2.next

        result = add_polynomials(result, temp_list)
        p1 = p1.next

    return result

def print_polynomial(poly):
    current = poly.next
    if not current:
        print("0")
        return "0"

    terms = []
    while current:
        coef = current.coef
        exp = current.exp

        if coef == 0:
            current = current.next
            continue

        term = ""
        if coef > 0 and terms:
            term += "+"
        elif coef < 0:
            term += "-"

        abs_coef = abs(coef)
        if abs_coef != 1 or exp == 0:
            term += str(abs_coef)

        if exp > 0:
            term += "x"
            if exp > 1:
                term += "^" + str(exp)

        terms.append(term)
        current = current.next

    if not terms:
        print("0")
        return "0"
    else:
        print("".join(terms))
        return "".join(terms)

def main():

    polyA = create_polynomial()

    polyB = create_polynomial()

    sum_poly = add_polynomials(polyA, polyB)
    product_poly = multiply_polynomials(polyA, polyB)


    print_polynomial(sum_poly)

    print_polynomial(product_poly)

if __name__ == "__main__":
    main()