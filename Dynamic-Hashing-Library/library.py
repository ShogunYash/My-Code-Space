import hash_table as ht

class DigitalLibrary:
    # DO NOT CHANGE FUNCTIONS IN THIS BASE CLASS
    def __init__(self):  
        pass
    
    def distinct_words(self, book_title):
        pass
    
    def count_distinct_words(self, book_title):
        pass
    
    def search_keyword(self, keyword):
        pass
    
    def print_books(self):
        pass
    
class MuskLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, book_titles, texts):
        self.books = []
        self.texts = []
        for text in texts:
            self.merge_sort(text)

        for text in texts:
            new_text = []
            new_text.append(text[0])
            for i in range(1,len(text)):
                if text[i] != text[i-1]:
                    new_text.append(text[i])
            self.texts.append(new_text)

        for i in range(len(book_titles)):
            self.books.append([book_titles[i], i])
        self.merge_sort(self.books)
        pass
    
    def distinct_words(self, book_title):
        index = self.binarySearch(self.books, 0, len(self.books)-1, book_title)
        return self.texts[index]     
    
    def count_distinct_words(self, book_title):
        distinct_words = self.distinct_words(book_title)
        return len(distinct_words)
    
    def search_keyword(self, keyword):
        book_titles = []
        for i in range(len(self.books)):
            index = self.books[i][1]
            boolean = self.binarySearch_keywords(self.texts[index], 0, len(self.texts[index])-1, keyword)
            if boolean:
                book_titles.append(self.books[i][0])
        return book_titles

    def print_books(self):
        for book, i in self.books:
            print(f"{book}: {' | '.join(self.texts[i])}")
        pass

    def binarySearch(self, arr, low, high, x):

        while low <= high:
            mid = low + (high - low) // 2
            # Check if x is present at mid
            y = arr[mid][0]
            if y > x:
                high = mid - 1      
            # If x is greater, ignore left half
            elif y < x:
                low = mid + 1
            # If x is smaller, ignore right half
            else:
                return arr[mid][1]
                
        return None

    def binarySearch_keywords(self, arr, low, high, x):

        while low <= high:
            mid = low + (high - low) // 2
            # Check if x is present at mid
            if arr[mid] == x:
                return True
            # If x is greater, ignore left half
            elif arr[mid] < x:
                low = mid + 1
            # If x is smaller, ignore right half
            else:
                high = mid - 1
                
        return False   

    def merge(self, arr, start, mid, end):
        # Create temporary arrays for the left and right halves
        left = arr[start:mid+1]
        right = arr[mid+1:end+1]
        
        i = j = 0  # Pointers for left and right arrays
        k = start  # Pointer for main array
        
        # Merge the two halves
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        # Copy any remaining elements from the left half
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        # Copy any remaining elements from the right half
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    # Iterative Merge Sort using an iterative approach
    def merge_sort(self, arr):
        n = len(arr)
        step = 1  # This controls the size of the subarrays we merge
        while step < n:
            for start in range(0, n - step, 2 * step):
                mid = start + step - 1
                end = min(start + 2 * step - 1, n - 1)
                # Merge the two subarrays arr[start:mid] and arr[mid+1:end]
                self.merge(arr, start, mid, end)
            step *= 2  # Increase step size to merge larger subarrays

class JGBLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, name, params):
        '''
        name    : "Jobs", "Gates" or "Bezos"
        params  : Parameters needed for the Hash Table:
            z is the parameter for polynomial accumulation hash
            Use (mod table_size) for compression function
            
            Jobs    -> (z, initial_table_size)
            Gates   -> (z, initial_table_size)
            Bezos   -> (z1, z2, c2, initial_table_size)
                z1 for first hash function
                z2 for second hash function (step size)
                Compression function for second hash: mod c2
        '''
        self.name = name
        self.params = params
        self.books = None
        self.hash_method = None
        if name == "Jobs": 
            self.books = ht.HashMap("Chain",params)
            self.hash_method = "Chain"
        elif name == "Gates":
            self.books = ht.HashMap("Linear",params)
            self.hash_method = "Linear"
        else:
            self.books = ht.HashMap("Double",params)
            self.hash_method = "Double"
        pass
    
    def add_book(self, book_title, text):
        value = ht.HashSet(self.hash_method, self.params)
        for word in text:
            value.insert(word)
        self.books.insert((book_title, value)) 
        pass
    
    def distinct_words(self, book_title):
        texts = self.books.find(book_title)
        new_text = []
        for text in texts.table:
            if text == "<EMPTY>":
                continue
            if isinstance(text, list):
                for word in text:
                    new_text.append(word)
            else:
                new_text.append(text)
        return new_text
    
    def count_distinct_words(self, book_title):
        texts = self.books.find(book_title)
        return texts.count
    
    def search_keyword(self, keyword):
        book_titles = []
        if self.hash_method == "Chain":
            for books in self.books.table:
                if books == "<EMPTY>":
                    continue
                for book in books:
                    if book[1].find(keyword):
                        book_titles.append(book[0])
        else:
            for book in self.books.table:
                if book == "<EMPTY>":
                    continue
                if book[1].find(keyword):
                    book_titles.append(book[0])      
        return book_titles
    
    def print_books(self):
        if self.hash_method == "Chain":
            for item in self.books.table:
                if item == "<EMPTY>":
                    continue
                for entry in item:
                    print(entry[0] + ": " + entry[1].__str__())
        else:
            for item in self.books.table:
                if item == "<EMPTY>":
                    continue
                print(item[0] + ": " +item[1].__str__())
        pass
        
