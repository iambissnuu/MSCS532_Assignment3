from randomized_quicksort import randomized_quicksort
from deterministic_quicksort import deterministic_quicksort
from hashtable_chaining import HashTable

print("Testing Randomized Quicksort:")
arr = [5, 2, 9, 1, 5, 6]
print("Original:", arr)
print("Sorted:", randomized_quicksort(arr))

print("\nTesting Deterministic Quicksort:")
arr2 = [3, 8, 2, 7, 4]
print("Original:", arr2)
print("Sorted:", deterministic_quicksort(arr2))

print("\nTesting HashTable with Chaining:")
ht = HashTable()
ht.insert("name", "Bishnu")
ht.insert("age", 25)
print("Search 'name':", ht.search("name"))
print("Delete 'age':", ht.delete("age"))
print("Search 'age':", ht.search("age"))
