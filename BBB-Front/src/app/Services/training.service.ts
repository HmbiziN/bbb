import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BASE_URL } from '../global/global';
import { TRAINING } from '../bbb';

@Injectable({
  providedIn: 'root'
})
export class TrainingService {

  constructor(
    private http: HttpClient
    ) { }
    
  public getAllTraining(){
    return this.http.get<TRAINING.training[]>(`${BASE_URL}/entrainement`,{
    })
  }

}
