from fastapi import FastAPI, HTTPException
from middleware.HandlerManager import HandlerManager
from request_schema.question import QuestionRequest
from request_schema.setup import CreateHandlerRequest
from threading import Thread


def start_garbage_collector():
    remaining_handlers = handler_manager.get_live_handlers()
    while remaining_handlers > 0:
        remaining_handlers = handler_manager.garbage_collect()


app = FastAPI()
handler_manager = HandlerManager(30)
gc_thread = Thread(target=start_garbage_collector, daemon=True)


@app.post("/handler/create")
def create_handler(request: CreateHandlerRequest):
    print("Request to create handler invoked")
    handler_id = handler_manager.add_handler(request.language)
    if not gc_thread.is_alive():
        gc_thread.start()
    return {"handler_id": handler_id}


@app.post("/ask")
def ask(request: QuestionRequest):
    try:
        handler = handler_manager.get_handler(request.handler_id)
        answer = handler.process_question(request.question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
