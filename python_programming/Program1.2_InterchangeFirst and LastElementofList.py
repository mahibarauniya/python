def main():
    A=[1, 2, 3, 4, 5]
    print("List A content is {}".format(A))
    first_element_in_array  = A[0]
    last_element_in_array   = A[-1]

    print("Before change: first element is {} and last element is {}".format(first_element_in_array,last_element_in_array))

    temp                   = first_element_in_array
    first_element_in_array = last_element_in_array
    last_element_in_array  = temp

    print("After change: first element is {} and last element is {}".format(first_element_in_array,last_element_in_array))

if __name__ == "__main__":
    main()