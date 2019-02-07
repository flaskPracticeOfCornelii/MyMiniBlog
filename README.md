# Mini Posting Blog

## I. Page Composition
1. root (/)
2. articles (/articles)
3. new (/articles/new) 
4. Detail content (/articles/id)
5. Edit (/articles/id/edit)


## II. Description

#### 1. root
* It only contain header, footer, and one button linked to articles page
* header & footer are conserved in all html page.

#### 2. articles
* This page shows each id and titles of articles.
* There is button to go to write up new post.("/articles/new")s

#### 3. new
* There are three text area in the form tag (from bootstrap)
* It act to send it values, in terms of POST way, to the ("/articles/new/create")

#### 4. Detail Content
* In the page of articles, each title is a tag to get user detailed content.
* And, by url It is accessable using its id
* It basically includes three buttons: Edit, Go-to-articles, Delete
* Delete button send its id to the ("/articles/id/delete")
* Edit button send its id to the ("/articles/id/edit")

#### 5. Edit
* It has the same format as new.
* Its origianl content is conserved in corresponding textarea.
* Last button in form tag send id to the ("/articles/id/update") to update database


#### 6. Remarks
* Common layout is saved in "layout.html". And, It was inherited by each html document according to jinja syntax.
* "header.html" and "footer.html" are separated from "layout.html". They are handled by including syntax of jinja
* Data base is named blog.db (sql)
* 