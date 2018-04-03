module Function where

import Data.List
import Data.Maybe

insertion_sort [] = []
insertion_sort (first:rest) = insertion_sort_helper rest [first]

insertion_sort_helper (first:rest) sorted = Nothing -- fill in
insert_in_order item left_list (first:rest) = Nothing -- fill in

binary_search list item offset = Nothing -- fill in

split_char string char = Nothing -- fill in
