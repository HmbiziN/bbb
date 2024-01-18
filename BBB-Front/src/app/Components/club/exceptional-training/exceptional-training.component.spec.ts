import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ExceptionalTrainingComponent } from './exceptional-training.component';

describe('ExceptionalTrainingComponent', () => {
  let component: ExceptionalTrainingComponent;
  let fixture: ComponentFixture<ExceptionalTrainingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ExceptionalTrainingComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ExceptionalTrainingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
