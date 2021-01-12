import { TestBed } from '@angular/core/testing';

import { EmployeesResolverService } from './employees-resolver.service';

describe('EmployeesResolverService', () => {
  let service: EmployeesResolverService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EmployeesResolverService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
