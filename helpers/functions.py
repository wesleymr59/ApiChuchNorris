#!/usr/bin/env python3
import os, requests
from fastapi import HTTPException

def convertTojson(bodyRequest):
        return bodyRequest.json()


def getRandon() -> dict:
        resultRequest = requests.get(os.environ['ENV_URL']+'/jokes/random')
        return convertTojson(resultRequest)


def getCategoria(categoria)-> dict:
        resultRequest = requests.get(os.environ['ENV_URL']+f'/jokes/random?category={categoria}')
        return resultRequest


def validaBody(convertBodyRequest)-> dict:
        if convertBodyRequest.get('value')!=None:
                return  convertBodyRequest['value']
        if 'status' in convertBodyRequest:
                raise HTTPException(status_code=404, detail=convertBodyRequest['message'])
        else:
                raise HTTPException(status_code=400, detail="bad request")

def buscaPorParametros(catgoria):
        bodyRequest = getCategoria(catgoria)
        convertBodyRequest = convertTojson(bodyRequest) 
    
        return validaBody(convertBodyRequest)
