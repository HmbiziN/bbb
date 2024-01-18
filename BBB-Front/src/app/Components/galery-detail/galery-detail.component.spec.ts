import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GaleryDetailComponent } from './galery-detail.component';

describe('GaleryDetailComponent', () => {
  let component: GaleryDetailComponent;
  let fixture: ComponentFixture<GaleryDetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GaleryDetailComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GaleryDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
