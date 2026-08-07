# Hash Map

## Time Complexities

Search: O(1) average

Insert: O(1)

Delete: O(1)

Worst case: O(n)

---

## Common Interview Problems

- Two Sum
- Valid Anagram
- Group Anagrams
- Longest Consecutive Sequence

---

## Common Mistakes

- Forgetting duplicates

- Using map instead of unordered_map

- Confusing key and value

---

## Pattern

Store previously seen elements.

For each element:

Check if the required complement already exists.

If yes, answer found.

Otherwise store current element.