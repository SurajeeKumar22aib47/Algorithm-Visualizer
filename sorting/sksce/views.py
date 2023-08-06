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
from django.shortcuts import render

def insertion_sort(request):
    if request.method == 'POST':
        input_list = list(map(int, request.POST.get('input_list', '').split(',')))
        steps = []

        def insertion_sort_recursive(arr):
            n = len(arr)
            for i in range(1, n):
                key = arr[i]
                j = i - 1
                while j >= 0 and key < arr[j]:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key
                steps.append({
                    'step_array': list(arr),
                    'explanation': f'Insert {key} into the correct position'
                })

        insertion_sort_recursive(input_list)

        context = {
            'input_list': input_list,
            'steps': steps,
        }

        return render(request, 'insertion_result.html', context)

    return render(request, 'insertion_sort.html')


def bubble_sort(request):
    if request.method == 'POST':
        input_list = list(map(int, request.POST.get('input_list', '').split(',')))
        steps = []

        def bubble_sort_recursive(arr):
            n = len(arr)
            for i in range(n):
                # Flag to check if any swap occurred during this iteration
                swapped = False
                for j in range(0, n - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        swapped = True
                        steps.append({
                            'step_array': list(arr),
                            'explanation': f'Swap {arr[j]} and {arr[j + 1]}'
                        })

                # If no swaps occurred in this iteration, the list is sorted
                if not swapped:
                    break

        bubble_sort_recursive(input_list)

        context = {
            'input_list': input_list,
            'steps': steps,
        }

        return render(request, 'bubble_result.html', context)

    return render(request, 'bubble_sort.html')




def merge_sort(request):
    if request.method == 'POST':
        input_list = list(map(int, request.POST.get('input_list', '').split(',')))
        steps = []

        def merge(arr, left, mid, right):
            left_arr = arr[left:mid+1]
            right_arr = arr[mid+1:right+1]
            i, j, k = 0, 0, left

            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] <= right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                else:
                    arr[k] = right_arr[j]
                    j += 1
                k += 1

            while i < len(left_arr):
                arr[k] = left_arr[i]
                i += 1
                k += 1

            while j < len(right_arr):
                arr[k] = right_arr[j]
                j += 1
                k += 1

        def merge_sort_recursive(arr, left, right):
            if left < right:
                mid = (left + right) // 2
                merge_sort_recursive(arr, left, mid)
                merge_sort_recursive(arr, mid + 1, right)
                merge(arr, left, mid, right)
                steps.append({
                    'step_array': list(arr),
                    'explanation': f'Merged subarrays from index {left} to {mid} and {mid+1} to {right}'
                })

        merge_sort_recursive(input_list, 0, len(input_list) - 1)

        context = {
            'input_list': input_list,
            'steps': steps,
        }

        return render(request, 'merge_result.html', context)

    return render(request, 'merge.html')

from django.shortcuts import render

def selection_sort(request):
    if request.method == 'POST':
        input_list = list(map(int, request.POST.get('input_list', '').split(',')))
        steps = []

        def selection_sort_recursive(arr):
            n = len(arr)
            for i in range(n):
                min_idx = i
                for j in range(i + 1, n):
                    if arr[j] < arr[min_idx]:
                        min_idx = j

                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                steps.append({
                    'step_array': list(arr),
                    'explanation': f'Swap {arr[i]} and {arr[min_idx]} (minimum element)'
                })

        selection_sort_recursive(input_list)

        context = {
            'input_list': input_list,
            'steps': steps,
        }

        return render(request, 'selection_result.html', context)

    return render(request, 'selection.html')


from django.shortcuts import render

def heap_sort(request):
    if request.method == 'POST':
        input_list = list(map(int, request.POST.get('input_list', '').split(',')))
        steps = []
        heap_size = len(input_list)

        def heapify(arr, n, i):
            largest = i
            left_child = 2 * i + 1
            right_child = 2 * i + 2

            if left_child < n and arr[i] < arr[left_child]:
                largest = left_child

            if right_child < n and arr[largest] < arr[right_child]:
                largest = right_child

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                steps.append({
                    'step_array': list(arr),
                    'explanation': f'Swap {arr[i]} and {arr[largest]} to satisfy the max heap property'
                })
                heapify(arr, n, largest)

        def build_max_heap(arr):
            for i in range(heap_size // 2 - 1, -1, -1):
                heapify(arr, heap_size, i)

        def heap_sort_recursive(arr):
            build_max_heap(arr)
            for i in range(heap_size - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]
                steps.append({
                    'step_array': list(arr),
                    'explanation': f'Swap {arr[i]} (root) and {arr[0]} to move the largest element to the end'
                })
                heapify(arr, i, 0)

        heap_sort_recursive(input_list)

        context = {
            'input_list': input_list,
            'steps': steps,
        }

        return render(request, 'heap_result.html', context)

    return render(request, 'heap.html')




from django.shortcuts import render

def quick_sort(request):
    if request.method == 'POST':
        input_list = list(map(int, request.POST.get('input_list', '').split(',')))
        steps = []

        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1

            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    steps.append({
                        'step_array': list(arr),
                        'explanation': f'Swap {arr[i]} and {arr[j]}'
                    })

            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            steps.append({
                'step_array': list(arr),
                'explanation': f'Swap {arr[i + 1]} (pivot) and {arr[high]}'
            })

            return i + 1

        def quick_sort_recursive(arr, low, high):
            if low < high:
                pivot_index = partition(arr, low, high)
                quick_sort_recursive(arr, low, pivot_index - 1)
                quick_sort_recursive(arr, pivot_index + 1, high)

        quick_sort_recursive(input_list, 0, len(input_list) - 1)

        context = {
            'input_list': input_list,
            'steps': steps,
        }

        return render(request, 'quick_result.html', context)

    return render(request, 'quick.html')

def generate_explanations(steps):
    explanations = []
    for step_num, step_list in steps:
        step_explanation = []
        step_explanation.append(f"Step {step_num + 1}:")
        step_explanation.append("We choose a pivot element and partition the list such that elements less than or equal to the pivot are to its left, and elements greater than the pivot are to its right.")
        step_explanation.append(f"Pivot: {step_list[-1]}")
        step_explanation.append(f"Current List: {step_list}")
        explanations.append(step_explanation)
    return explanations
