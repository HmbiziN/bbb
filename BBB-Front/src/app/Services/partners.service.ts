import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BASE_URL } from '../global/global';
import { CLUB } from '../bbb';
@Injectable({
  providedIn: 'root'
})
export class PartnersService {

  constructor(private http: HttpClient) { }

  public getAllPartners(){
    return this.http.get<CLUB.Partners[]>(`${BASE_URL}/partenaire`,{
    })
  }

}
