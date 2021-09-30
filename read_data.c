#include <stdio.h>
#include <string.h>


#define BUFFER_SIZE 100


int main(){
    FILE* filePointer = fopen("adresse.csv","r");
    char charArray[BUFFER_SIZE];
    int nbl = 0;
    int nbc = 0;
    int i = 0;
    int j = 0;
    


    if (filePointer == NULL) {
       printf("Adress doesnt exist !\n");
       return -1;
    }

    while (fgets(charArray, BUFFER_SIZE, filePointer) != NULL) {
        nbl = nbl + 1;
    }


    rewind(filePointer);
    fgets(charArray, BUFFER_SIZE, filePointer);
    char* ptr = strtok(charArray, ",");
    while(ptr != NULL){
        nbc = nbc+1;
        ptr = strtok(NULL, ",");
    }
    
    char* dataArray[nbl][nbc];

    rewind(filePointer);
    while (fgets(charArray, BUFFER_SIZE, filePointer) != NULL) {       
        char* ptr = strtok(charArray, ",");
        while(j < nbc){
            dataArray[i][j] = ptr;
            printf("'%s'\n", dataArray[i][j]);
            ptr = strtok(NULL,",");
            j = j+1;
        }
        i = i + 1;
        j = 0;
    }

    return 0;
}







