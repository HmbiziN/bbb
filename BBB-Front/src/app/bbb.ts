export namespace CLUB {
  export interface Actu {
    id:number,
    title: string,
    date: Date,
    content: string,
    img: string
  }
  export interface Pole {
    id: number,
    role: string,
    team: string,
    prenom: string,
    nom: string,
    img: string
  }
  export interface Partners{
    id: number;
    img: string;
  }
  export interface Licence {
    id:number;
    prix:number;
    categorie:string
  }
  export interface Coordinates {
    name: string;
    adress: string;
    lat: number;
    lng: number;
  }
}

export namespace DASHBOARD{
  export interface Result extends Upcoming{
  } 
  export interface Upcoming{
    id:number;
    equipe_1: string;
    equipe_2: string;
    Date: Date;
    section: number;
    score: number;
    a_venir:boolean;
  }

}

export namespace PLAYER{
  export interface team{
    id: number;
    nom: string;
    photo: string;
    section: number;
  }
  export interface section{
    id: number;
    title: string;
    description: string;
  }
}

export namespace PICTURES{
  export interface Album{
    id: number;
    titre: string;
    description: string;
    couverture: string
  }
  export interface Photo{
    id: number;
    titre: string;
    img: string;
  }
}

export namespace TRAINING{
  export interface training extends PLAYER.team{
    id:number;
    date: Date;
    debut: number;
    fin: number;
    frequence: string;
    jour: string;
    salle: string
  }
}






