import { TestBed } from '@angular/core/testing';

import { SharedDashboardService } from './shared-dashboard.service';

describe('SharedDashboardService', () => {
  let service: SharedDashboardService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SharedDashboardService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
