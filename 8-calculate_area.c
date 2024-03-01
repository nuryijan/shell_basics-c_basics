#include <stdio.h>
#include <stdlib.h>

/**
 * main - calculate the area of a rectangle
 *
 * Return: Always 0 (Success)
 */
int main(void)
{
  float width = 0;
  float height = 0;

  printf("Enter the width of the rectangle: ");
  scanf("%f", &width);

  printf("Enter the height of the rectangle: ");
  scanf("%f", &height);
  /* Your code gode here */

  float area = height * width;
  printf("The area of the rectangle is: %.2f\n", area);

  return 0;
}
