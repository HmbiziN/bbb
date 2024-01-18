import {
  HttpClient
} from '@angular/common/http';
import {
  Component,
  OnInit
} from '@angular/core';
import {
  FormGroup,
  Validators,
  FormControl
} from '@angular/forms';
import {
  BASE_URL
} from 'src/app/global/global';

@Component({
  selector: 'app-contact-page',
  templateUrl: './contact-page.component.html',
  styleUrls: ['./contact-page.component.css']
})
export class ContactPageComponent implements OnInit {
  public contactForm: FormGroup;
  public expediteur: string = '';
  public telephone: number = 0;
  public prenom: string = '';
  public nom: string = '';
  public message: string = '';
  public errorFields: boolean = false;
  public successMessage: boolean = false;

  constructor(
    private http: HttpClient
  ) {}
  ngOnInit(): void {
    this.contactForm = new FormGroup({
      expediteur: new FormControl('', [Validators.required, Validators.email]),
      telephone: new FormControl('', [Validators.required, Validators.pattern("[0-9 ]{10}")]),
      prenom: new FormControl('', [Validators.required, Validators.minLength(3)]),
      nom: new FormControl('', [Validators.required, Validators.minLength(3)]),
      message: new FormControl('', [Validators.required, Validators.minLength(30)]),
    })
  }

  public submit() {
    this.errorFields = !this.contactForm.valid;
    if (this.contactForm.valid) {
      this.postDataFormContact(this.contactForm.value);
    }
  }

  public postDataFormContact(contact) {
    this.http.post(BASE_URL + '/contact-form/', {
        titre: 'Demande de Contact',
        message: contact.message,
        prenom: contact.prenom,
        nom: contact.nom,
        telephone: contact.telephone,
        expediteur: contact.expediteur
      })
      .subscribe({
        next: () => this.successMessage = true,
        error: (e) => console.log(e)
      })
  }
}
