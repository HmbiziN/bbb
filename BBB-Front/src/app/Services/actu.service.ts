import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { CLUB } from '../bbb';
import { BASE_URL } from '../global/global';

@Injectable({
  providedIn: 'root'
})
export class ActuService {

  constructor(
    private http: HttpClient
  ) { }

  public getActu(){
    return this.http.get<CLUB.Actu []>(`${BASE_URL}/actu`,{
    })
  }
}
