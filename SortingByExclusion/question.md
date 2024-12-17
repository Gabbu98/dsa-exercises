# Sorting By Exclusion

# Minimum Words Removal for Lexicographic Order

## **Task**

Given a non-empty list (or array, depending on the programming language) of non-empty uppercase words, the goal is to compute the minimum number of words to remove so that the remaining words are in strictly ascending lexicographic order.

---

## **Rules**

1. Words are considered strictly ascending if each word is lexicographically larger than the previous one.
2. Equal elements are not regarded as sorted. To ensure strict ordering, duplicates must be reduced to one or removed entirely.

---

## **Examples**

### Example 1:

Input:

```css
css
Copy code
["THE", "QUICK", "BROWN", "FOX", "JUMPS", "OVER", "THE", "LAZY", "DOG"]

```

Output:

```
Copy code
4

```

Explanation:

Remove `"THE"`, `"QUICK"`, `"LAZY"`, and `"DOG"`. The remaining sorted list is:

```css
css
Copy code
["BROWN", "FOX", "JUMPS", "OVER", "THE"]

```

---

### Example 2:

Input:

```css
css
Copy code
["JACKDAW", "LOVE", "MY", "BIG", "SPHINX", "OF", "QUARTZ"]

```

Output:

```
Copy code
2

```

Explanation:

Remove `"BIG"` and `"SPHINX"`. The remaining sorted list is:

```css
css
Copy code
["JACKDAW", "LOVE", "MY", "OF", "QUARTZ"]

```

---

### Example 3:

Input:

```css
css
Copy code
["A", "A", "A", "A"]

```

Output:

```
Copy code
3

```

Explanation:

Remove all but one `"A"`. The remaining sorted list is:

```css
css
Copy code
["A"]

```

---

## **Approach**

This problem can be solved by finding the **Longest Increasing Subsequence (LIS)** in the input list and calculating the words that must be removed to achieve the sorted list:

Words to remove=Total words−Length of LIS\text{Words to remove} = \text{Total words} - \text{Length of LIS}

Words to remove=Total words−Length of LIS

---

## **Algorithm**

1. Initialize a list `lis` of size equal to the input list, with all values set to `1`.
    - `lis[i]` will store the length of the longest increasing subsequence ending at index `i`.
2. Iterate through the list with two nested loops:
    - Outer loop (`i`) iterates through the list from `1` to `n-1`.
    - Inner loop (`j`) iterates from `0` to `i-1` and checks:
        - If `words[j] < words[i]` (lexicographic comparison).
        - If extending the subsequence ending at `words[j]` results in a longer subsequence for `words[i]`.
3. Update `lis[i]` to reflect the new longest subsequence length.
4. Find the maximum value in `lis`, which is the length of the longest increasing subsequence.
5. Calculate the result:Minimum words to remove=len(words)−max(lis)
    
    Minimum words to remove=len(words)−max(lis)\text{Minimum words to remove} = \text{len(words)} - \text{max(lis)}
    

---

## **Complexity**

- **Time Complexity**: O(n2) due to the nested loop for computing LIS.
    
    O(n2)O(n^2)
    
- **Space Complexity**: O(n) for storing the `lis` array.
    
    O(n)O(n)
    

For very large inputs, the LIS calculation can be optimized using a binary search approach to achieve O(nlog⁡n)O(n \log n)O(nlogn).