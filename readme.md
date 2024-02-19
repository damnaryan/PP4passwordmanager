## This is a learning project.
I am making this project to learn python.So, instead of learing the syntax first, I am building this project to learn while I am building this. I have made notes within the code as comments, of every new concept I get to know.
##### Source of learning: https://www.youtube.com/watch?v=NpmFbWO6HPU&list=WL
### About this project:
This is a password manager.

### [IN PROGRESS]

## Learnings:
- **Opening a file in pyhton:**
  Syntax #1
  *with open('filename.xyz', 'open_mode') as f:*
    *----------*
    *----------*
  Syntax #2
  *f = open('filename.xyz', 'open_mode')*
  *f.close()*

  Syntax #1 is better for opening a file, as for with 'with' cmd, the file opens and closes automatically after everthing intended under 'with' is completed. Upon normally opening the file, it needs to closed after the work is done.
  Open modes are mainly of three types: 'r' for read-only mode, 'w' for overwrite mode and 'a' for append mode. Append mode is more versetile than the overwrite mode as append mode makes changes without deleting the present data in the file whereas the overwrite mode clears the slate clean to make new changes.

- *.readlines()* attribute: used to store a single line from a text. (Usually from a file for ex: a txt file)
  Syntax
  *f = readme.txt*
  *print(f.readlines())*
  *print(f.readlines())*
  Output
  *line1*
  *line2*

- Litte bit of encryption. (This code has incomplete encruption.)

- 