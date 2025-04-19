#include <stdlib.h>
#include <string.h>
#include "substring.h"

/**
 * struct WordCount - Simple structure to count words
 * @word: the word
 * @count: how many times it should appear
 */
typedef struct WordCount
{
    char *word;
    int count;
} WordCount;

/**
 * find_word - finds a word in the WordCount array
 */
int find_word(WordCount *wc, int size, const char *word)
{
    for (int i = 0; i < size; i++)
        if (strcmp(wc[i].word, word) == 0)
            return i;
    return -1;
}

/**
 * find_substring - main logic to find valid starting indexes
 */
int *find_substring(char const *s, char const **words, int nb_words, int *n)
{
    int word_len, total_len, s_len, *indices = NULL, idx_count = 0;
    WordCount *expected, *seen;
    char *word;

    *n = 0;
    if (!s || !words || nb_words == 0)
        return NULL;

    word_len = strlen(words[0]);
    total_len = word_len * nb_words;
    s_len = strlen(s);

    expected = malloc(sizeof(WordCount) * nb_words);
    if (!expected)
        return NULL;

    // Count expected words
    int unique = 0;
    for (int i = 0; i < nb_words; i++)
    {
        int j = find_word(expected, unique, words[i]);
        if (j != -1)
            expected[j].count++;
        else
        {
            expected[unique].word = strdup(words[i]);
            expected[unique].count = 1;
            unique++;
        }
    }

    // Sliding window
    for (int i = 0; i <= s_len - total_len; i++)
    {
        seen = malloc(sizeof(WordCount) * unique);
        for (int k = 0; k < unique; k++)
        {
            seen[k].word = expected[k].word;
            seen[k].count = 0;
        }

        int j;
        for (j = 0; j < nb_words; j++)
        {
            word = strndup(s + i + j * word_len, word_len);
            int pos = find_word(expected, unique, word);
            free(word);
            if (pos == -1)
                break;

            seen[pos].count++;
            if (seen[pos].count > expected[pos].count)
                break;
        }

        if (j == nb_words)
        {
            indices = realloc(indices, sizeof(int) * (idx_count + 1));
            indices[idx_count++] = i;
        }

        free(seen);
    }

    for (int i = 0; i < unique; i++)
        free(expected[i].word);
    free(expected);

    *n = idx_count;
    return indices;
}
