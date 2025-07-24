#include <stdio.h>

struct Student {
    char name[20];
    int age;
    float grade;
};

int main() {
    struct Student students[3];
    int i, top_index = 0;

    // Read data for 3 students
    for (i = 0; i < 3; i++) {
        printf("Enter name of student %d: ", i + 1);
        scanf("%s", students[i].name);

        printf("Enter age of student %d: ", i + 1);
        scanf("%d", &students[i].age);

        printf("Enter grade of student %d: ", i + 1);
        scanf("%f", &students[i].grade);

        printf("\n");
    }

    // Find the student with the highest grade
    for (i = 1; i < 3; i++) {
        if (students[i].grade > students[top_index].grade) {
            top_index = i;
        }
    }

    // Print the name of the student with the highest grade
    printf("Student with the highest grade is: %s\n", students[top_index].name);

    return 0;
}
