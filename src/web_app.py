import linecache
from typing import List
import fastapi
import os
from model import NoteInfoResponse
from model import NoteTextResponse
from model import NoteCreateResponse
from model import NoteListResponse
from model import NoteDeleteResponse
from model import NoteUpdateResponse
import datetime
import random
import string
api_router = fastapi.APIRouter()

@api_router.post("/create_note", response_model = NoteCreateResponse)
def create_note(text: str, token: str):
    t = linecache.getline('tokens.txt', 1)
    t = t.split()
    t = t[1]
    if token == t:
        f1 = os.listdir("notes")
        m_id = []
        for i in range(len(f1)):
            a: list[str] = f1[i].split(".")
            m_id.append(a[0])
            p = int(max(m_id))
            id = p + 1
        my_file = open('notes/' + str(id) + ".txt", "w+")
        my_file.write(text)
        letters = string.ascii_lowercase
        token = ''.join(random.sample(letters, 4))
        t = open("tokens.txt", "a")
        line = str('\n' + str(id) + ". " + token)
        t.write(line)

        return NoteCreateResponse(
            id = int(id),
        )
    else:
        return NoteCreateResponse(
            id = 0
        )


@api_router.get("/read_note", response_model = NoteTextResponse)
def read_note(id: str, token: str):
    file1 = open("tokens.txt", "r")
    lines = file1.readlines()
    for line in lines:
        a = line.split(". ")
        b = a[1].split("\n")
        if a[0] == str(id):
            t = b[0]

    if token == t:
        my_file = open('notes/' + str(id) + ".txt", "r")
        text = my_file.read()

        return NoteTextResponse(
        id = int(id),
        text = str(text)
        )

    else:
        return NoteTextResponse(
            id = 0
        )

@api_router.delete("/delete_note", response_model = NoteDeleteResponse)
def delete_note(id: int, token: str):
    file1 = open("tokens.txt", "r")
    lines = file1.readlines()
    for line in lines:
        a = line.split(". ")
        b = a[1].split("\n")
        if a[0] == str(id):
            t = b[0]

    if token == t:
        os.remove('notes/' + str(id) + ".txt")

        return NoteDeleteResponse(
        id = int(id)
        )
    else:
        return NoteDeleteResponse(
        id = 0
        )

@api_router.put("/update_note", response_model = NoteUpdateResponse)
def update_note(id: int, text: str, token: str):
    file1 = open("tokens.txt", "r")
    lines = file1.readlines()
    for line in lines:
        a = line.split(". ")
        b = a[1].split("\n")
        if a[0] == str(id):
            t = b[0]

    if token == t:
        my_file = open('notes/' + str(id) + ".txt", "w+")
        my_file.write(text)

        return NoteUpdateResponse(
        id = int(id)
        )
    else:
        return NoteUpdateResponse(
        id = 0
        )

@api_router.get("/list_note", response_model = NoteListResponse)
def list_note(token: str):
    t = linecache.getline('tokens.txt', 1)
    t = t.split()
    t = t[1]
    if token == t:
        f1 = os.listdir("notes")
        m_id = []
        for i in range(len(f1)):
            a = f1[i].split(".")
            m_id.append(int(a[0]))

        return NoteListResponse(
        note_list = m_id
        )
    else:
        return NoteListResponse(
        note_list = " "
        )

@api_router.get("/info_note", response_model = NoteInfoResponse)
def info_note(id: int, token: str):
    file1 = open("tokens.txt", "r")
    lines = file1.readlines()
    for line in lines:
        a = line.split(". ")
        b = a[1].split("\n")
        if a[0] == str(id):
            t = b[0]

    if token == t:
        path = r"notes/" + str(id) + ".txt"
        time_c = datetime.datetime.fromtimestamp(os.path.getctime(path))
        time_u = datetime.datetime.fromtimestamp(os.path.getmtime(path))

        return NoteInfoResponse(
        created_at = time_c,
        updated_at = time_u
        )
    else:
        return NoteInfoResponse(
        created_at = 0,
        updated_at = 0
        )