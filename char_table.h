#ifndef CHAR_TABLE
#define CHAR_TABLE

/***********************************************************************
INCLUDE
***********************************************************************/
#include <stdio.h>
/***********************************************************************
DEFINE
***********************************************************************/
#define data_wordlength 10
#define input_wordlength 10
#define N 256
/***********************************************************************
STRUCTER
***********************************************************************/
//入力された文字と頻度を格納する構造体
typedef struct KEYWORD{
    char keywords[data_wordlength];
    int frest;
    struct KEYOWORD *next;
}KEYWORD;

//単語の一覧を格納する構造体
typedef struct FREG{
    char wordst[input_wordlength];
}FREG;

//単語表（全ての情報）
typedef struct FREGTABLE{
    FREG table[N];
    KEYWORD keytable[N];
    KEYWORD newtable[N];
    int wordnext;
    int keynext;
    int newnext;
}FREGTABLE;

//入力された文字と頻度を格納するリスト構造体
typedef struct LIST{
    char keywords[data_wordlength];
    int frest;
    struct LIST *next;
}LIST;

/***********************************************************************
FUNCTION PROTOTYPE
***********************************************************************/
extern void CTPut(FREGTABLE *fregtable);
extern void CreateNewCT(FREGTABLE *fregtable);
extern void SORTChar(FREGTABLE *fregtable);
extern void SORTFreg(FREGTABLE *fregtable);
extern LIST ListCreate(FREGTABLE *fregtable,LIST *listtable,int k,int accnum);

#endif