# Challenge#1 
## Tetris


Johnny is playing a weird kind of TETRIS. He has already worked out the pseudo-random number generator used in the game, so that he knows exactly what pieces will appear on the field – one by one. He has also discovered the exact scoring rules.


## Description of the weird TETRIS


The field has 5 columns; there is a floor at the bottom, but its height is unlimited.

Each piece consists of 3 squares which are positioned vertically in one of the columns. Each square is assigned a colour.

The pieces drop vertically down (from a very great height) until they hit an obstacle (floor or other piece).

The player may not modify a given piece, then the piece drops into a column in which it has appeared on the field.

The player can modify (change) a given piece. It can be done in two ways:  

⦁ by changing the column in which the piece is positioned; or

⦁ by rotating the piece.

![Alt text](1603190969_pic1.png?raw=true)

Picture img 1 shows an original position of an exemplary piece consisting of squares A, B and C, placed in column 1. If the player does not intervene, the piece will drop onto the bottom (img 2).


The piece can be moved to any column (an example for column 4 is shown in img 3, and the effect after the piece descends is shown in img 4).


The player can also make a colour rotation. The single rotation is shown in img 5, and the duoble rotation is visible in img 6.


Naturally, it is possible to combine both types of modification an example of which can be seen in img 7 (it is still a modification of one block). 

 


The aim of the game is to complete lines with a length of at least 3 squares of the same colour. The lines can be horizontal, vertical, or diagonal.


When the piece descends onto the field, all single-colour lines are detected. After that, any square that belongs to at least one line disappears; the remaining squares drop freely, and the lines are detected again.


Everything is repeated until there is no single-colour line on the field.


The example below shows the next stages of the field after a block drops.


![Alt text](1603190998_pic2.png?raw=true)


In img 1, we can see a block dropping.

In img 2, the state of the field after the piece drops is shown.

In img 3, the completed lines are marked: one horizontal (with a length of 4 squares) and one diagonal (with a length of 3 squares).

In img 4, we can see the field after the squares belonging to the marked lines have been cleared.

In img 5, the state of the field after all remaining squares on the field descend. This is where the first stage of field clearing ends.


We begin the next stage. In img 6, we can see four lines completed: two vertical (with a length of 3 squares), one horizontal (with a length of 5 squares), and one diagonal (with a length of 3 squares).

Picture img 7 shows the state after the disappearance of the squares from the marked lines, while in img 8, we can see the state of the field after the second stage of field clearing.


It is also the last stage because there are no single-colour lines on the field.


## Scoring


For each completed line, the player gets some points. Obviously, the longer the line, the more points the player gets. Moreover, in the weird TETRIS (as in any other), the completion of several lines at the same time guarantees some extra points. What is more, the field clearing in several stages is rewarded.


The base points for completing a line with a length of n squares are equal to n2. Points for lines completed in the same stage are added up. Then the sum of the points is multiplied by the number of completed lines (there is a bonus for completing a large number of lines). The result obtained is multiplied by the stage number (there is a bonus for a large number of field clearing stages).


The value obtained in this way means the number of points awarded for a specific stage of field clearing.

The total number of points for a given piece is the sum of points for each stage.

The score for the entire game is the total of points obtained for each piece.

![Alt text](1603191181_pic3.png?raw=true)

In the example above, the scoring is as follows:

- Stage 1:

⦁ two lines (with lengths of 3 and 4 squares), hence the base points are equal to 3 * 3 + 4 * 4 = 25;

⦁ the base result is multiplied by the number of lines: 25 * 2 = 50;

⦁ the whole is multiplied by the stage number: 50 * 1 = 50.

- Stage 2:

⦁ four lines (three with a length of 3 squares and one with a length of 5 squares), hence the base points are equal to 3 * 3 + 3 * 3 + 3 * 3 + 5 * 5 = 9 + 9 + 9 + 25 = 52;

⦁ the base result is multiplied by the number of lines: 52 * 4 = 208;

⦁ the whole is multiplied by the stage number: 208 * 2 = 416.


The total number of points for the piece is equal to 50 + 416 = 466.


Yet another example:



⦁ Stage 1: one line with a length of 3 squares; base points: 9, multiplying by the number of lines: 9 * 1 = 9, multiplying by the stage number: 9 * 1 = 9.

⦁ Stage 2: one line with a length of 3 squares; base points: 9, multiplying by the number of lines: 9 * 1 = 9, multiplying by the stage number: 9 * 2 = 18.

⦁ Stage 3: one line with a length of 3 squares; base points: 9, multiplying by the number of lines: 9 * 1 = 9, multiplying by the stage number: 9 * 3 = 27.

⦁ Stage 4: four lines with a length of 3 squares; base points: 9 * 4 = 36, multiplying by the number of lines: 36 * 4 = 144, multiplying by the stage number: 144 * 4 = 576.

⦁ Stage 5: two lines with a length of 3 squares; base points: 9 * 2 = 18, multiplying by the number of lines: 18 * 2 = 36, multiplying by the stage number: 36 * 5 = 180.


Total score: 9 + 18 + 27 + 576 + 180 = 810.


## Task:



Write a function

int getMaxScore(int count, int up[], int mid[], int down[], int col[], int changeCount);


The count parameter means the number of blocks in the game.


The up, mid, down, and col arrays contain the description of the subsequent pieces. The piece number i (for 0 <= i < count) consists of three squares of the colours up[i] (top square), mid[i] (middle square) and down[i] (bottom square), and is placed in col[i] column.


The parameters described above determine the subsequent pieces that appear in the game.


Johnny wants to impress his friends and plans to interfere with a maximum of changeCount pieces throughout the game. This means that only in the case of changeCount pieces, he can change the column and/or rotate the piece. The remaining pieces will drop onto the field in places and rotation compatible with the data contained in the parameters of the getMaxScore function.


The function should calculate one value: the maximum number of points that can be obtained according to the given rules.


Constraints:


1 <= up[i], mid[i], down[i] <= 1000000000;

0 <= col[i] <= 4;

0 <= changeCount <= 2;

1 <= count <= 80 - 30 * changeCount;

maximum number of getMaxScore function calls: 5.


## Example:

![Alt text](1603193215_pic4.png?raw=true)


Let’s consider the following function call (img 1):

getMaxScore(2, [2,1], [1,2], [1,1], [1,3], changeCount);


 


For changeCount = 0, no line is completed, hence the result is equal to 0 (img 2).


For changeCount = 1, we can move the first piece to the third column. Additionally, we need to rotate the moved piece. We have one line with a length of 3 squares (img 3), hence the result is equal to 9. It is worth noting that the change of the column and the rotation of one block count as one change.


For changeCount = 2, we can modify both pieces. It is best to position them in one column and rotate them to complete a line with a length of 4 squares (img 4). Hence the result is equal to 16.
