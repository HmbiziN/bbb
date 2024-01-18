import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BASE_URL } from '../global/global';
import { DASHBOARD } from '../bbb';

@Injectable({
  providedIn: 'root'
})
export class ResultService {

  constructor(
    private http: HttpClient
    ) { }

  public  getResult(){
    return this.http.get<DASHBOARD.Result[]>(`${BASE_URL}/match`,{
    })
  }
}
