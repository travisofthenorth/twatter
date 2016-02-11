## Setting up

Install dependencies

```bash
pip install -r requirements.txt
```

Set up database (assuming postgres is installed)

```bash
createdb twatter
psql twatter < schema.sql
```

Usage

```bash
python twatter.py 'donald trump' 'kanye west' 'chicken nuggets'
```
