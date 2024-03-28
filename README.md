# PLaGue

PLaGue is a highly personalized password generator. This tool permits to create a list of 
password based on patterns. It's possible to create and add a pattern among those already available.

## How to use it 

In PLaGue, there are three types of elements that can be added to the password list: ranges, special characters, and words. 

A **range** is a sequence of numbers defined by a start and an end value. For example, a range of 1 to 5 would include the numbers 1, 2, 3, 4, and 5. The syntax to add a range is the following :
[{start_number}...{end_number}]

A **special character** is a character that is not a letter or a number. Examples of special characters include punctuation marks, such as the exclamation point (!) and the at symbol (@). 
You can find the total list of special character in the section Special Characters

A **word** is a sequence of characters that typically represents a unit of meaning in a language. In this application, a word can be any sequence of characters, only including letters.

 Once PLaGue is launched, you can add several elements to generate password.
 Every section of element has the following possible actions:
 
1. **Add Elements**: To add an element, click on the "+" button in the respective sections to add an element. 
   
2. **Delete Elements**: To delete an element, select it in the list and click on the "🗑" button.
   
3. **Import Elements**: You can also import elements from a text file by clicking on the "📁" button.

Once you achieved completing all elements, you need to select generators. A generator is a tool that creates a password list based on a set of rules. The generator uses a combination of words, numbers (ranges), and special characters to create the password list.

There are different types of generators available in the application, each with its own name and description. Every generator creates passwords using a combination of a word, a number and a special character. 

Every generator has its own requirements, that means that a generator can require a single or a combination of elements. For example some generators can require only words and ranges, others can require words, ranges and special characters.

Once generators are selected you can generate the password list by clicking 'Generate password list'. You can now select the output directory of your file and the password list will be generated and named `pwd_list.txt`.