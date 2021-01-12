import { TestBed } from '@angular/core/testing';

import { AllowedRolesGuardService } from './allowed-roles-guard.service';

describe('AllowedRolesGuardService', () => {
  let service: AllowedRolesGuardService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AllowedRolesGuardService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
