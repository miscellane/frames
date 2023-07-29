# Testing

<br>

### Notes ($In$ $Progress$)

Explore the base image

```bash
docker run --rm -i -t -p 10000:8888 jupyter/base-notebook
```

```bash
docker run --rm -i -t -p 10000:8888 -v ~/library/miscellane/frames jupyter/base-notebook
```

<br>

Extend the base image via a `Dockerfile` ...

```bash
docker build -t notebook .
```

```bash
docker run --rm -i -t -p 127.0.0.1:10000:8888 -w /app --mount type=bind,src="$(pwd)",target=/app notebook
```

```bash
docker run -i -t -p 127.0.0.1:10000:8888 -w /app --mount type=bind,src="$(pwd)",target=/app notebook
```

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>