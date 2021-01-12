import { TestBed } from '@angular/core/testing';

import { CurrentUserStateService } from './current-user-state.service';

describe('CurrentUserStateService', () => {
  let service: CurrentUserStateService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CurrentUserStateService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
