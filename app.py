from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory='templates')

def generate_content(topic:str):
    return {
        'ideas':[f'{topic}热门选题{i}' for i in range(1,6)],
        'titles':[f'为什么{topic}越来越火？', f'{topic}新手避坑指南', f'做{topic}的人都知道的秘密'],
        'script': f'开场3秒吸引注意，今天聊聊{topic}...最后引导关注。',
        'post': f'如果你也关注{topic}，这篇内容建议收藏。'
    }

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "data": None})

@app.post("/", response_class=HTMLResponse)
async def run(request: Request, topic: str = Form(...)):
    data = generate_content(topic)
    return templates.TemplateResponse("index.html", {"request": request, "data": data, "topic": topic})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
