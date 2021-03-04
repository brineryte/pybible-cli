"""
{
  "_Bible__books": [
    {
      "_Book__author": "John, the Apostle",
      "_Book__chapters": {
        "py/tuple": [
          {
            "_Chapter__number": 1,
            "_Chapter__verses": {
              "py/tuple": [
                {
                  "_Verse__number": 1,
                  "_Verse__text": "That which was from the beginning, which we have heard, which we have seen with our eyes, which we have looked upon, and our hands have handled, of the Word of life;",
                  "py/object": "pybible.classes.verse.Verse"
                }
              ]
            },
            "py/object": "pybible.classes.chapter.Chapter"
          },
        ]
      },
      "_Book__full_title": "The First Epistle General of John",
      "_Book__title": "1 John",
      "py/object": "pybible.classes.book.Book"
    }
  ],
  "_Bible__language": "English",
  "_Bible__name": "King James Bible",
  "_Bible__ot_last_book": 39,
  "py/object": "pybible.classes.bible.Bible"
}
"""

import json
import itertools

BOOK_TEMPLATE = {"_Bible__books": [
    {"_Book__author": "author", "_Book__chapters": {"py/tuple": []}, "_Book__full_title": "fulltitle",
     "_Book_title": "title", "py/object": "pybible.classes.book.Book"}], "_Bible__language": "English",
    "_Bible__name": "translation",
    "_Bible__ot_last_book": 39,
    "py/object": "pybible.classes.bible.Bible"}
CHAPTER_TEMPLATE = {"_Chapter__number": 0, "_Chapter__verses": {"py/tuple": []},
                    "py/object": "pybible.classes.chapter.Chapter"}
VERSE_TEMPLATE = {"_Verse__number": 0, "_Verse__text": "verse", "py/object": "pybible.classes.verse.Verse"}


# loop through books (web) dir,
# for each book, open the WEB book json and use the file name to get the kjv json as well
# use the above templates to build the new json, filling in the missing information
# kjv will provide book title, full title, and book author
# web will provide book chapters and verses


with open('resources/bibles_json/web/1john.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

verses = [verse for verse in data if "verseNumber" in verse.keys()]


def key_func(k):
    return k['chapterNumber']


chapters = sorted(verses, key=key_func)

for key, value in itertools.groupby(chapters, key_func):
    print(key)
    print(list(value))
