from django.shortcuts import render




# Create your views here.
def home(request):
    return render(request,'home.html')

def linear_search(request):
    if request.method == 'POST':
        input_list = request.POST.get('input_list', '').split(',')
        search_element = request.POST.get('search_element', '')

        found_index = -1
        steps = []  # Step-by-step list to keep track of each step in the search process.

        for index, element in enumerate(input_list):
            step = {
                'index': index,
                'element': element.strip(),
                'found': False
            }

            if element.strip() == search_element:
                found_index = index
                step['found'] = True

            steps.append(step)

        if found_index == -1:
            found_index = "no element"

        context = {
            'input_list': input_list,
            'search_element': search_element,
            'found_index': found_index,
            'steps': steps,  # Include the steps list in the context.
        }

        return render(request, 'linear_result.html', context)

    return render(request, 'linear.html')

def binary_search(request):
    if request.method == 'POST':
        input_list = request.POST.get('input_list', '').split(',')
        search_element = request.POST.get('search_element', '')
        sorted_input_list = sorted(input_list)
        left = 0
        right = len(sorted_input_list) - 1
        binary_found_index = -1
        steps = []  # Step-by-step list to keep track of each step in the binary search process.

        while left <= right:
            mid = (left + right) // 2
            step = {
                'left': left,
                'right': right,
                'mid': mid,
                'mid_element': sorted_input_list[mid].strip(),
                'found': False
            }

            if sorted_input_list[mid].strip() == search_element:
                binary_found_index = mid
                step['found'] = True
                break
            elif sorted_input_list[mid].strip() < search_element:
                left = mid + 1
            else:
                right = mid - 1

            steps.append(step)

        context = {
            'input_list': input_list,
            'search_element': search_element,
            'binary_found_index': binary_found_index,
            'steps': steps,  # Include the steps list in the context.
        }
        return render(request, 'binary_result.html', context)

    return render(request, 'binary.html')

def insertion_sort(request):
    if request.method == 'POST':
        input_list = request.POST.get('input_list', '').split(',')

        input_list = [int(item.strip()) for item in input_list]
        steps = []  # Step-by-step list to keep track of each step in the insertion sort process.

        for i in range(1, len(input_list)):
            key = input_list[i]
            j = i - 1

            step = {
                'current_list': input_list[:],  # Create a copy of the current list for the step.
                'key': key,
                'sorted_elements': input_list[:i],
                'swap': False
            }

            while j >= 0 and input_list[j] > key:
                input_list[j + 1] = input_list[j]
                j -= 1
                step['swap'] = True

            input_list[j + 1] = key
            steps.append(step)

        context = {
            'input_list': request.POST.get('input_list', ''),
            'steps': steps,  # Include the steps list in the context.
        }

        return render(request, 'insertion_result.html', context)

    return render(request, 'insertion_sort.html')
def bubble_sort(request):
    if request.method == 'POST':
        input_list = request.POST.get('input_list', '').split(',')
        input_list = [int(item.strip()) for item in input_list]
        steps = []  # Step-by-step list to keep track of each step in the bubble sort process.

        for i in range(len(input_list)):
            swapped = False
            for j in range(len(input_list) - i - 1):
                step = {
                    'current_list': input_list[:],  # Create a copy of the current list for the step.
                    'swap': False
                }
                if input_list[j] > input_list[j + 1]:
                    input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
                    step['swap'] = True
                    swapped = True
                steps.append(step)

            # If no swaps happened during the inner loop, the list is already sorted.
            if not swapped:
                break

        context = {
            'input_list': request.POST.get('input_list', ''),
            'steps': steps,  # Include the steps list in the context.
        }

        return render(request, 'bubble_result.html', context)

    return render(request, 'bubble_sort.html')



def merge_sort(request):
    if request.method == 'POST':
        input_list = list(map(int, request.POST.get('input_list', '').split(',')))

        def merge_sort_recursive(lst, steps):
            if len(lst) <= 1:
                return lst

            mid = len(lst) // 2
            left = merge_sort_recursive(lst[:mid], steps)
            right = merge_sort_recursive(lst[mid:], steps)

            merged_list = []
            left_index, right_index = 0, 0

            step = {
                'left': left[:],
                'right': right[:],
                'merged': [],
            }

            while left_index < len(left) and right_index < len(right):
                if left[left_index] <= right[right_index]:
                    merged_list.append(left[left_index])
                    left_index += 1
                else:
                    merged_list.append(right[right_index])
                    right_index += 1

            merged_list += left[left_index:]
            merged_list += right[right_index:]

            step['merged'] = merged_list
            steps.append(step)

            return merged_list

        steps = []  # Step-by-step list to keep track of each step in the merge sort process.
        sorted_list = merge_sort_recursive(input_list, steps)

        context = {
            'input_list': input_list,
            'sorted_list': sorted_list,
            'steps': steps,  # Include the steps list in the context.
        }

        return render(request, 'merge_result.html', context)

    return render(request, 'merge.html')


def selection_sort(request):
    if request.method == 'POST':
        input_list = list(map(int, request.POST.get('input_list', '').split(',')))

        steps = []  # Step-by-step list to keep track of each step in the selection sort process.

        for i in range(len(input_list)):
            min_index = i
            for j in range(i + 1, len(input_list)):
                if input_list[j] < input_list[min_index]:
                    min_index = j

            input_list[i], input_list[min_index] = input_list[min_index], input_list[i]

            # Save a copy of the current list for this step.
            steps.append(input_list[:])

        context = {
            'input_list': input_list,
            'steps': steps,  # Include the steps list in the context.
        }

        return render(request, 'selection_result.html', context)

    return render(request, 'selection.html')

def heap_sort(request):
    if request.method == 'POST':
        input_list = list(map(int, request.POST.get('input_list', '').split(',')))

        def heapify(arr, n, i, steps):
            largest = i
            left_child = 2 * i + 1
            right_child = 2 * i + 2

            if left_child < n and arr[i] < arr[left_child]:
                largest = left_child

            if right_child < n and arr[largest] < arr[right_child]:
                largest = right_child

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest, steps)

            # Save a copy of the current list for this step.
            steps.append(arr[:])

        def heap_sort_recursive(arr, steps):
            n = len(arr)

            for i in range(n // 2 - 1, -1, -1):
                heapify(arr, n, i, steps)

            for i in range(n - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]
                heapify(arr, i, 0, steps)

        steps = []  # Step-by-step list to keep track of each step in the heap sort process.
        heap_sort_recursive(input_list, steps)

        context = {
            'input_list': input_list,
            'steps': steps,  # Include the steps list in the context.
        }

        return render(request, 'heap_result.html', context)

    return render(request, 'heap.html')

def quick_sort(request):
    if request.method == 'POST':
        input_list = list(map(int, request.POST.get('input_list', '').split(',')))

        def partition(arr, low, high, steps):
            pivot = arr[high]
            i = low - 1

            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[high] = arr[high], arr[i + 1]

            # Save a copy of the current list for this step.
            steps.append(arr[:])

            return i + 1

        def quick_sort_recursive(arr, low, high, steps):
            if low < high:
                pi = partition(arr, low, high, steps)

                quick_sort_recursive(arr, low, pi - 1, steps)
                quick_sort_recursive(arr, pi + 1, high, steps)

        steps = []  # Step-by-step list to keep track of each step in the quicksort process.
        quick_sort_recursive(input_list, 0, len(input_list) - 1, steps)

        context = {
            'input_list': input_list,
            'steps': steps,  # Include the steps list in the context.
        }

        return render(request, 'quick_result.html', context)

    return render(request, 'quick.html')
